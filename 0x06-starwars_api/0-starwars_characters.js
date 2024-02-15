#!/usr/bin/node

const req = require('request');
const id_movie = process.argv[2];
const film_EP = 'https://swapi-api.hbtn.io/api/films/' + id_movie;
let people = [];
const names = [];
