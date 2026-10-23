__version__ = '0.26.0.post2+musa5.2.0'
git_version = 'da055cc1c2ae59da7780251e20b4c263a36adcf9'
from torchvision.extension import _check_cuda_version
if _check_cuda_version() > 0:
    cuda = _check_cuda_version()
