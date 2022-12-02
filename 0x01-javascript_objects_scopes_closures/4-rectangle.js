#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = parseInt(w);
      this.height = parseInt(h);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const somevar = this.width;
    this.width = this.height;
    this.height = somevar;
  }

  double () {
    this.width = this.height * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;