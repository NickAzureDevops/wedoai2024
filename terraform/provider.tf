terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=3.30.0"
    }
  }
  backend "azurerm" {
  }
}

provider "azurerm" {
  skip_provider_registration = true
  features {
  }
}

provider "azuread" {
}

data "azurerm_client_config" "current" {}