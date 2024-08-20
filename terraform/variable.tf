variable "location" {
  default = "UK South"
}

variable "context" {
  description = "The context for the deployment"
  type        = string
  default     = "dev"
}

variable "name" {
  description = "The name of the resource group"
  type        = string
  default     = "wedoAI-demo-2025-rg"
}