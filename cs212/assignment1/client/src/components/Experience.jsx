import React from 'react';
import { Row, Col } from 'react-bootstrap';

function Experience({ experience }) {
  return (
    <div className="resume-section">
      <h2>Experience</h2>
      {experience.map((exp) => (
        <div key={exp.id} className="resume-item">
          <Row>
            <Col md={8}>
              <h3 className="company">{exp.company}</h3>
              <h4>{exp.position}</h4>
              <p>{exp.description}</p>
            </Col>
            <Col md={4} className="text-md-end">
              <span className="year">{exp.year}</span>
            </Col>
          </Row>
        </div>
      ))}
    </div>
  );
}

export default Experience;