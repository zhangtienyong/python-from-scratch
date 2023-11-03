import os

# Get a specific environment variable
env_variable = os.environ.get("YOUR_ENV_VARIABLE_NAME")

# Print all environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")
