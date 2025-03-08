import React from 'react';
import { Row, Col } from 'react-bootstrap';

function Education({ education }) {
  return (
    <div className="resume-section">
      <h2>Education</h2>
      {education.map((edu) => (
        <div key={edu.id} className="resume-item">
          <Row>
            <Col md={8}>
              <h3 className="institution">{edu.institution}</h3>
              <h4>{edu.degree}</h4>
              <p>{edu.description}</p>
            </Col>
            <Col md={4} className="text-md-end">
              <span className="year">{edu.year}</span>
            </Col>
          </Row>
        </div>
      ))}
    </div>
  );
}

export default Education;