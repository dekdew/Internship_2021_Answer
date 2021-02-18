var express = require("express");
var router = express.Router();
var crawler = require("../utils/Crawler");

crawler.getCompanies().then((resolve) => {
  const companies = resolve;

  /* GET companies listing. */
  router.get("/", function (req, res, next) {
    res.json(companies);
  });
});

module.exports = router;
