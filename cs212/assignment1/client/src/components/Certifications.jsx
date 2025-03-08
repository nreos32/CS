import React from 'react';
import { Row, Col } from 'react-bootstrap';

function Certifications({ certifications }) {
  return (
    <div className="resume-section">
      <h2>Certifications</h2>
      <div className="resume-item">
        {certifications.map((cert) => (
          <Row key={cert.id} className="mb-3">
            <Col md={8}>
              <h4>{cert.name}</h4>
              <p>Issued by: {cert.issuer}</p>
            </Col>
            <Col md={4} className="text-md-end">
              <span className="year">{cert.year}</span>
            </Col>
          </Row>
        ))}
      </div>
    </div>
  );
}

export default Certifications;