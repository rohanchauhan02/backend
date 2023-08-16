package models

import "github.com/golang-jwt/jwt"

type UserJWT struct {
	ID       uint   `json:"id"`
	Username string `json:"username"`
	Email    string `json:"email"`
	jwt.StandardClaims
}
