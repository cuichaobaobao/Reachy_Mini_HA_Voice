import unittest
from pathlib import Path


class ProjectIdentityTests(unittest.TestCase):
    def test_home_assistant_device_metadata_is_neutral(self):
        source = Path("reachy_mini_ha_voice/protocol/message_dispatch.py").read_text()
        self.assertIn("project_name=\"reachy-mini.ha-voice\"", source)
        self.assertIn("manufacturer=\"Reachy Mini HA Voice\"", source)
        self.assertIn("model=\"Voice Satellite\"", source)
        self.assertNotIn("lichao" + "622.Reachy Mini HA Voice", source)
        self.assertNotIn("manufacturer=\"" + "lichao" + "622\"", source)

    def test_user_docs_do_not_expose_personal_device_namespace(self):
        for path in [Path("README.md"), Path("docs/USER_MANUAL_CN.md"), Path("docs/USER_MANUAL_EN.md")]:
            text = path.read_text()
            self.assertNotIn("lichao" + "622.Reachy Mini HA Voice", text)
            self.assertNotIn("Manufacturer: `" + "lichao" + "622`", text)
            self.assertNotIn("制造商：`" + "lichao" + "622`", text)


if __name__ == "__main__":
    unittest.main()
