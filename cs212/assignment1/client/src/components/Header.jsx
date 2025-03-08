import React from 'react';
import { Container } from 'react-bootstrap';

function Header({ overview }) {
  return (
    <header className="text-center py-5 bg-light">
      <Container>
        <h1>{overview.name}</h1>
        <h2>{overview.title}</h2>
      </Container>
    </header>
  );
}

export default Header;