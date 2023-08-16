package util

import (
	"github.com/fgrosse/goldi"
	"github.com/jinzhu/gorm"
	"github.com/labstack/echo"
	"github.com/rohanchauhan2/loan-service/models"
	"github.com/rohanchauhan2/loan-service/shared/config"
)

type CustomApplicationContext struct {
	echo.Context
	Container    *goldi.Container
	SharedConfig config.ImmutableConfigInterface
	MysqlSession *gorm.DB
	UserJWT      *models.UserJWT
}
