#!/usr/bin/node

const { resolve } = require('path');
const req = require('request');
const id_movie = process.argv[2];
const film_EP = 'https://swapi-api.hbtn.io/api/films/' + id_movie;
let people = [];
const names = [];

const requestChar = async () => {
  await new Promise(resolve => req(film_EP, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      people = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (people.length > 0) {
    for (const p of people) {
      await new Promise(resolve => req(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  }
}
