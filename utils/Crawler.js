var Crawler = require("crawler");

var uri = "https://theinternship.io/";

const getCompanies = () => {
  return new Promise((resolve, reject) => {
    var c = new Crawler();
    var companies = [];
    c.direct({
      uri: uri,
      callback: function (error, res) {
        if (error) {
          reject(error);
        } else {
          var companiesSrc = res.$(".logo-box img").map(function () {
            return this.attribs.src;
          });

          var companiesText = res.$(".box-textbox span").map(function () {
            return this.children[0].data;
          });

          for (var i = 0; i < companiesSrc.length; i++) {
            companies.push({ src: companiesSrc[i], text: companiesText[i] });
          }

          companies.sort((a, b) => (a.text.length > b.text.length ? 1 : -1));

          const sortedCompanies = {
            companies: companies.map((company) => ({
              logo: `https://theinternship.io/${company["src"]}`,
            })),
          };

          resolve(sortedCompanies);
        }
      },
    });
  });
};

module.exports.getCompanies = getCompanies;
