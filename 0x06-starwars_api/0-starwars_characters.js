#!/usr/bin/node

const request = require('request');

const parseToJson = (obj) => {
  try {
    return JSON.parse(obj);
  } catch (err) {
    return null;
  }
};

const getMovieCharacter = (characterUrls) => {
  if (!characterUrls.length) return;

  request.get(characterUrls[0], (err, res, body) => {
    if (err) throw new Error(err);

    const character = parseToJson(body);
    if (character) console.log(character.name);

    getMovieCharacter(characterUrls.slice(1));
  });
};

const getMovieCharaterUrls = (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}`;

  request.get(url, (err, res, body) => {
    if (err) throw new Error('Failed to make request');
    const movieCharacters = JSON.parse(body).characters;

    getMovieCharacter(movieCharacters);
  });
};

getMovieCharaterUrls(3);
