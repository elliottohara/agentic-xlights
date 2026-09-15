import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch, MagicMock
import urllib.error
from Tools.setup_song import setup_song
from Tools import xlights_api as x


class SongSetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.show = Path(self.temp.name).resolve() / 'Test Show'
        self.show.mkdir()
        (self.show / 'xlights_rgbeffects.xml').write_text('<xrgb/>')
        (self.show / 'Faces').mkdir()

    def test_independent_layout_links_and_preserved_customization(self):
        song = setup_song(self.show, 'New Song')
        layout = song / 'xlights_rgbeffects.xml'
        self.assertFalse(layout.is_symlink())
        self.assertEqual((song / 'Faces').readlink(), Path('../../Faces'))
        self.assertEqual((song / 'Faces').resolve(), self.show / 'Faces')
        self.assertEqual(list(song.glob('*.xsq')), [])
        layout.write_text('<song-specific/>')
        (song / 'AGENT NOTES.md').write_text('Reviewed order')
        setup_song(self.show, 'New Song')
        self.assertEqual(layout.read_text(), '<song-specific/>')
        self.assertEqual((song / 'AGENT NOTES.md').read_text(), 'Reviewed order')
        self.assertEqual((self.show / 'xlights_rgbeffects.xml').read_text(), '<xrgb/>')
        other = setup_song(self.show, 'Other Song')
        self.assertEqual((other / 'xlights_rgbeffects.xml').read_text(), '<xrgb/>')

    def test_invalid_names_missing_master(self):
        for name in ('', '..', '../escape', 'a/b', 'a\\b', ' newline\n'):
            with self.assertRaises(ValueError):
                setup_song(self.show, name)
        (self.show / 'xlights_rgbeffects.xml').unlink()
        with self.assertRaises(ValueError):
            setup_song(self.show, 'New Song')
        self.assertFalse((self.show / 'Sequences').exists())

    def test_refuses_layout_link_to_master(self):
        song = self.show / 'Sequences' / 'Linked'
        song.mkdir(parents=True)
        (song / 'xlights_rgbeffects.xml').symlink_to('../../xlights_rgbeffects.xml')
        with self.assertRaises(ValueError):
            setup_song(self.show, 'Linked')
        self.assertFalse((song / 'Media').exists())

    def test_refuses_redirected_sequences(self):
        (self.show / 'Sequences').symlink_to(self.temp.name, target_is_directory=True)
        with self.assertRaises(ValueError):
            setup_song(self.show, 'Escape')


class ApiTests(unittest.TestCase):
    def response(self, payload):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = json.dumps(payload).encode()
        return response

    def test_preserves_face_name(self):
        with patch.object(x.urllib.request, 'urlopen', return_value=self.response({'worked': True})) as call:
            x.add_effect('Singer', 0, 'Faces', 'FaceDefinition=Teddy ', '', 0, 1000)
        request = call.call_args.args[0]
        self.assertEqual(json.loads(request.data)['settings'], 'FaceDefinition=Teddy ')
        self.assertTrue(request.full_url.endswith('/xlDoAutomation'))

    def test_detects_boolean_and_string_failures(self):
        for payload in ({'worked': False}, {'worked': 'false'}, {'res': 503}):
            with patch.object(x.urllib.request, 'urlopen', return_value=self.response(payload)):
                with self.assertRaises(RuntimeError):
                    x.xl('addEffect')

    def test_no_automatic_mutation_retry(self):
        error = urllib.error.HTTPError(x.BASE, 503, 'busy', {}, None)
        with patch.object(x.urllib.request, 'urlopen', side_effect=error) as call:
            with self.assertRaises(urllib.error.HTTPError):
                x.xl('addEffect')
        self.assertEqual(call.call_count, 1)

    def test_rejects_corrupting_command_relative_save(self):
        with self.assertRaises(ValueError):
            x.xl('setEffectSettings')
        with self.assertRaises(ValueError):
            x.save('Song.xsq')

    def test_preview_parent_exists_before_request(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'Previews' / 'test.mp4'
            def check(cmd, **kwargs):
                self.assertTrue(path.parent.is_dir())
                self.assertEqual(cmd, 'exportVideoPreview')
                return {'res': 200}
            with patch.object(x, 'xl', side_effect=check):
                x.export_video_preview(path)


if __name__ == '__main__':
    unittest.main()
