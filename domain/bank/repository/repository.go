package repository

import "github.com/jinzhu/gorm"

type repoHandler struct {
	mysqlSession *gorm.DB
}

func NewBankRepository(mysqlSession *gorm.DB) *repoHandler {
	return &repoHandler{
		mysqlSession: mysqlSession,
	}
}

func (r *repoHandler) CreateBank() error {
	return nil
}
