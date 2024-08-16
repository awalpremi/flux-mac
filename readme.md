I have an M2 Ultra with 192GB of ram, but you should be ok with 20 something GB.

# Flux

Welcome to Flux, an AI-powered game developed by LLC. This readme file will guide you through the installation and usage of Flux.

## Getting Started

To get started, follow these steps:

1. Open up your terminal.

2. Create a new Conda environment with Python 3.11:

    ```shell
    conda create -n flux-env python=3.11 -y
    ```

3. Activate the Conda environment:

    ```shell
    conda activate flux-env
    ```

4. Install DiffusionKit using pip:

    ```shell
    pip install git+https://github.com/argmaxinc/DiffusionKit.git
    ```

## Usage

Once you have installed Flux, you can use the following command to run it:

```shell
diffusionkit-cli \
  --prompt "a photo of a cat" \
  --output-path image.png \
  --model-version FLUX.1-schnell \
  --steps 4
```

Please note that the command above is just an example. Feel free to change the prompt, output path, model version, and steps according to your needs.

## Wait for Weights

After running the command, please wait for the weights to be downloaded. This may take some time depending on your internet connection.

## Image Manipulation

Once the weights are downloaded, you can perform various image manipulations using the following options:

- Minimize image
- Edit image
- Delete image
- Maximize image

Feel free to choose any option based on your requirements.

## Acknowledgements

Special thanks to Awni Hannun and the teams at Apple and Argmax for their contributions.


