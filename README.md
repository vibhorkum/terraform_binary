# Python wrapper for Terraform binary

This is a Python wrapper for Hashicorp's Terraform. Using `terraform_binary` you can install Terraform using Pipenv or Pip, instead of manually downloading, unzipping and installing it.

## Usage

```sh
pipenv install terraform-binary

terraform init # Now you can use terraform, after you installed it with Pipenv or Pip.
```

## Build wheel

Works only on Mac/Linux for distributing since we need to set the execution rights of the binaries properly. Windows doesnt allow this.

```sh
build-wheel.sh
```

## License

This project is [Apache License Version 2.0](LICENSE).
