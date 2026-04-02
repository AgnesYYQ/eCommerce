# Cognito User Pool for authentication
resource "aws_cognito_user_pool" "users" {
  name = "ecommerce-users"

  password_policy {
    minimum_length    = 8
    require_uppercase = true
    require_lowercase = true
    require_numbers   = true
    require_symbols   = false
  }

  auto_verified_attributes = ["email"]
}

resource "aws_cognito_user_pool_client" "users_client" {
  name         = "ecommerce-users-client"
  user_pool_id = aws_cognito_user_pool.users.id
  generate_secret = false
  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_flows = ["code"]
  allowed_oauth_scopes = ["email", "openid", "profile"]
  callback_urls = ["https://your-frontend-domain.com/callback"]
  logout_urls   = ["https://your-frontend-domain.com/logout"]
  supported_identity_providers = ["COGNITO"]
}

resource "aws_cognito_user_pool_domain" "users_domain" {
  domain       = "ecommerce-users-domain"
  user_pool_id = aws_cognito_user_pool.users.id
}
