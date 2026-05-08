import torch
import torchvision.utils as vutils

from model import Generator

device = torch.device("cpu")

G = Generator().to(device)

G.load_state_dict(
    torch.load(
        "generator.pth",
        map_location=device
    )
)

G.eval()

def generate_face():

    noise = torch.randn(
        1,
        100,
        1,
        1,
        device=device
    )

    with torch.no_grad():

        fake = G(noise).detach().cpu()

    vutils.save_image(
        fake,
        "static/generated/output.png",
        normalize=True
    )