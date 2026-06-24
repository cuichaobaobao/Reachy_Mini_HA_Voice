"""Entity registry for ESPHome entities.

This module handles the registration and management of all ESPHome entities
for the Reachy Mini voice assistant.
"""

import logging
from collections.abc import Callable
from typing import TYPE_CHECKING

from ..models import Preferences
from .entity_extensions import SwitchEntity
from .entity_keys import get_entity_key
from .runtime_entity_setup import (
    setup_behavior_entities,
    setup_runtime_entities,
    setup_service_entities,
)
from .sensor_entity_setup import (
    append_defined_entities,
    setup_audio_direction_entities,
    setup_imu_entities,
    setup_motion_entities,
    setup_robot_info_entities,
)

if TYPE_CHECKING:
    from ..reachy_controller import ReachyController

_LOGGER = logging.getLogger(__name__)


class EntityRegistry:
    """Registry for managing ESPHome entities."""

    def __init__(
        self,
        server,
        reachy_controller: "ReachyController",
        play_emotion_callback: Callable[[str], None] | None = None,
    ):
        """Initialize the entity registry.

        Args:
            server: The VoiceSatelliteProtocol server instance
            reachy_controller: The ReachyController instance
            play_emotion_callback: Optional callback for playing emotions
        """
        self.server = server
        self.reachy_controller = reachy_controller
        self._play_emotion_callback = play_emotion_callback

        # Emotion state
        self._current_emotion = "None"
        # Curated HA-facing emotions. The robot still has a larger internal
        # library, but exposing everything made the HA device page noisy.
        self._emotion_map = {
            "None": None,
            "Happy": "cheerful1",
            "Sad": "sad1",
            "Angry": "rage1",
            "Surprise": "surprised1",
            "Curious": "curious1",
            "Thoughtful": "thoughtful1",
            "Tired": "tired1",
            "Yes": "yes1",
            "No": "no1",
            "Oops": "oops1",
            "Come": "come1",
            "Sleep": "sleep1",
            "Dance": "dance1",
        }

    def _get_preferences(self) -> Preferences | None:
        return self.server.state.preferences

    def _get_server_state(self):
        return self.server.state

    def _save_preferences(self) -> None:
        self.server.state.save_preferences()

    def _set_preference_and_save(self, key: str, value) -> None:
        prefs = self._get_preferences()
        if prefs is not None:
            setattr(prefs, key, value)
            self._save_preferences()

    def _get_pref_bool(self, key: str, default: bool = False) -> bool:
        prefs = self._get_preferences()
        return bool(getattr(prefs, key, default)) if prefs is not None else default

    def _set_pref_bool(self, key: str, enabled: bool) -> None:
        prefs = self._get_preferences()
        if prefs is not None:
            setattr(prefs, key, bool(enabled))
            self._save_preferences()

    def _set_idle_behavior_enabled(self, enabled: bool) -> None:
        self.reachy_controller.set_idle_behavior_enabled(enabled)

        prefs = self._get_preferences()
        if prefs is not None:
            prefs.set_idle_behavior_enabled(enabled)
            self._save_preferences()

    def _make_preference_switch(
        self,
        *,
        key_name: str,
        name: str,
        object_id: str,
        icon: str,
        getter: Callable[[], bool],
        setter: Callable[[bool], None],
    ) -> SwitchEntity:
        """Create a switch entity with the common registry wiring."""
        return SwitchEntity(
            server=self.server,
            key=get_entity_key(key_name),
            name=name,
            object_id=object_id,
            icon=icon,
            entity_category=1,
            value_getter=getter,
            value_setter=setter,
        )

    def _make_stored_switch(
        self,
        *,
        key_name: str,
        name: str,
        object_id: str,
        icon: str,
        pref_key: str,
        getter_transform: Callable[[bool], bool] | None = None,
        setter_transform: Callable[[bool], bool] | None = None,
        after_set: Callable[[], None] | None = None,
    ) -> SwitchEntity:
        """Create a switch backed by preferences with optional transforms/hooks."""

        def getter() -> bool:
            value = self._get_pref_bool(pref_key)
            return getter_transform(value) if getter_transform is not None else value

        def setter(enabled: bool) -> None:
            stored = setter_transform(enabled) if setter_transform is not None else enabled
            self._set_pref_bool(pref_key, stored)
            if after_set is not None:
                after_set()

        return self._make_preference_switch(
            key_name=key_name,
            name=name,
            object_id=object_id,
            icon=icon,
            getter=getter,
            setter=setter,
        )

    def _append_defined_entities(
        self,
        entities: list,
        definitions: list,
        callback_map: dict[str, tuple[Callable, Callable] | Callable],
    ) -> None:
        """Bind callbacks to declarative definitions and append created entities."""
        append_defined_entities(self, entities, definitions, callback_map)

    def setup_all_entities(self, entities: list) -> None:
        """Setup all entity phases."""
        self._setup_phase1_entities(entities)
        self._setup_phase2_entities(entities)
        self._setup_phase3_entities(entities)
        self._setup_phase4_entities(entities)
        self._setup_phase5_entities(entities)  # DOA for wakeup turn-to-sound
        self._setup_phase6_entities(entities)
        self._setup_phase7_entities(entities)
        self._setup_phase8_entities(entities)
        self._setup_phase9_entities(entities)
        # Phase 11 (LED control) disabled - LEDs are inside the robot and not visible
        self._setup_phase12_entities(entities)
        # Phase 14 (head_joints, passive_joints) removed - not needed
        # Phase 20 (Tap detection) disabled - too many false triggers
        self._setup_phase21_entities(entities)

        _LOGGER.info("All entities registered: %d total", len(entities))

    def _setup_phase1_entities(self, entities: list) -> None:
        setup_runtime_entities(self, entities)

    def _setup_phase2_entities(self, entities: list) -> None:
        setup_service_entities(self, entities)

    def _setup_phase3_entities(self, entities: list) -> None:
        setup_motion_entities(self, entities)

    def _setup_phase4_entities(self, entities: list) -> None:
        pass

    def _setup_phase5_entities(self, entities: list) -> None:
        setup_audio_direction_entities(self, entities)

    def _setup_phase6_entities(self, entities: list) -> None:
        setup_robot_info_entities(self, entities)

    def _setup_phase7_entities(self, entities: list) -> None:
        setup_imu_entities(self, entities)

    def _setup_phase8_entities(self, entities: list) -> None:
        setup_behavior_entities(self, entities)

    def _setup_phase9_entities(self, entities: list) -> None:
        """Setup Phase 9 entities: Audio controls."""
        _LOGGER.debug("Phase 9 entities registered: none")

    def _setup_phase12_entities(self, entities: list) -> None:
        """Setup Phase 12 entities: Audio processing parameters."""
        _LOGGER.debug("Phase 12 entities registered: none")

    def _setup_phase21_entities(self, entities: list) -> None:
        pass

    def find_entity_references(self, entities: list) -> None:
        """Find and store references to special entities from existing list.

        Args:
            entities: The list of existing entities to search
        """
        # DOA entities are read-only sensors, no special references needed
        pass
