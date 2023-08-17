package models

import "github.com/golang-jwt/jwt"

type UserJWT struct {
	Username string `json:"username"`
	jwt.StandardClaims
}
