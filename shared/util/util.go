package util

import (
	"github.com/fgrosse/goldi"
	"github.com/go-playground/validator/v10"
	"github.com/jinzhu/gorm"
	"github.com/labstack/echo"
	"github.com/rohanchauhan02/loan-service/models"
	"github.com/rohanchauhan02/loan-service/shared/config"
)

type CustomApplicationContext struct {
	echo.Context
	Container    *goldi.Container
	SharedConfig config.ImmutableConfigInterface
	MysqlSession *gorm.DB
	UserJWT      *models.UserJWT
}

type CutomValidator struct {
	Validator *validator.Validate
}

func (c *CutomValidator) Validate(i interface{}) error {
	return c.Validator.Struct(i)
}

func DefaultValidator() *CutomValidator {
	return &CutomValidator{Validator: validator.New()}
}
