from diffusionkit.mlx import FluxPipeline


pipeline = FluxPipeline(
  model="argmaxinc/stable-diffusion",
  shift=1.0,
  model_version="FLUX.1-schnell",
  low_memory_mode=True,
  a16=True,
  w16=True,
)


HEIGHT = 400
WIDTH = 800
NUM_STEPS = 4  #  4 for FLUX.1-schnell, 50 for SD3
CFG_WEIGHT = 0. # for FLUX.1-schnell, 5. for SD3

image, _ = pipeline.generate_image(
  "a photo of a cat",
  cfg_weight=CFG_WEIGHT,
  num_steps=NUM_STEPS,
  latent_size=(HEIGHT // 8, WIDTH // 8),
)