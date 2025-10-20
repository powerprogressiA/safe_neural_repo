from hal import mock_interfaces

def test_mock_eeg_sensor():
    data = mock_interfaces.mock_eeg_sensor()
    assert "channels" in data
    assert len(data["channels"]) == 3

def test_mock_camera_frame():
    frame = mock_interfaces.mock_camera_frame()
    assert "pixels" in frame
    assert all(isinstance(p, int) for p in frame["pixels"])
