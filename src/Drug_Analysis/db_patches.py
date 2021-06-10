#!/usr/bin/env python
"""
contains all the patches that have been applied to
the database in order to keep schemas consistent across environments
"""


class DBPatch():
    def __init__(self, name, sql, validation, *args, **kwargs):
        """ Encapsulates the patches to be applied """
        self.name = name
        self.sql = sql
        self.validation = validation

patches = []

sql = """
    ALTER TABLE `dark_web`.`tblProduct`
    ADD COLUMN `USD` DECIMAL(15,2) UNSIGNED NULL COMMENT '' AFTER `product_picture`,
    ADD COLUMN `GBP` DECIMAL(15,2) UNSIGNED NULL COMMENT '' AFTER `USD`;
    """

validation = """
    SELECT *
    FROM information_schema.COLUMNS
    WHERE
        TABLE_SCHEMA = 'dark_web'
        AND TABLE_NAME = 'tblProduct'
        AND COLUMN_NAME = 'GBP';
        """
additional_currencies_patch = DBPatch(
    name='additional_currencies_patch',
    sql=sql,
    validation=validation
)


sql = """
CREATE TABLE `dark_web`.`tblUnit` (
  `unit_id` INT NOT NULL COMMENT '',
  `product_id` INT NOT NULL COMMENT '',
  `value` VARCHAR(45) NOT NULL COMMENT '',
  `unit_type` VARCHAR(45) NOT NULL COMMENT '',
  `purity` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`unit_id`)  COMMENT '',
  INDEX `fk_tblUnit_1_idx` (`product_id` ASC)  COMMENT '',
  CONSTRAINT `fk_tblUnit_1`
    FOREIGN KEY (`product_id`)
    REFERENCES `dark_web`.`tblProduct` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""

validation = """
    SELECT *
    FROM tblProduct;
    """

units_table_patch = DBPatch(
    name='additional_currencies_patch',
    sql=sql,
    validation=validation
)


patches.append(additional_currencies_patch)
patches.append(units_table_patch)


def db_patches_list():
    """ Returns a list containing all the patches required by the project """
    return patches
