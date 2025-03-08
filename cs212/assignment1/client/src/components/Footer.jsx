import React from 'react';
import { Container } from 'react-bootstrap';

function Footer() {
  return (
    <footer>
      <Container>
        <p className="mb-0">© {new Date().getFullYear()}</p>
      </Container>
    </footer>
  );
}

export default Footer;