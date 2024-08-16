import subprocess

command = [
    "conda", "activate", "diffusionkit"
]

subprocess.run(command)

command = [
    "diffusionkit-cli",
    "--prompt", "cat creating a linkedin header using a terminal on a mac",
    "--output-path", "linkedin.png",
    "--model-version", "FLUX.1-schnell",
    "--steps", "4",
    "--height", "400",
    "--width", "800",
]

subprocess.run(command)