resource "azurerm_resource_group" "rg" {
  name     = var.name
  location = var.location
}

resource "random_string" "this" {
  length  = 8
  special = false
  upper   = false
}

resource "azurerm_storage_account" "storage" {
  name                     = "wedoai2024${random_string.this.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = var.context
  }
}

resource "azurerm_application_insights" "insights" {
  name                = "wedoai2024${random_string.this.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = "web"
}

resource "azurerm_machine_learning_workspace" "ml_workspace" {
  name                    = "wedoai2024${random_string.this.result}"
  location                = azurerm_resource_group.rg.location
  resource_group_name     = azurerm_resource_group.rg.name
  application_insights_id = azurerm_application_insights.insights.id
  key_vault_id            = azurerm_key_vault.vault.id
  storage_account_id      = azurerm_storage_account.storage.id

  identity {
    type = "SystemAssigned"
  }
}

