#!/usr/bin/node

const req = require('request');
const id_movie = process.argv[2];
const film_EP = 'https://swapi-api.hbtn.io/api/films/' + id_movie;
let people = [];
const names = [];

const requestChar = async () => {
    await new Promise(resolve => req(film_EP, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error('Error: ', err, '| StatusCode: ', res.statusCode);
      }
    }))
  }