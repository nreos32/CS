import React from 'react';

function Skills({ skills }) {
  return (
    <div className="resume-section">
      <h2>Skills</h2>
      <div className="resume-item">
        {skills.map((skillCategory) => (
          <div key={skillCategory.id} className="mb-3">
            <h4 className="skill-category">{skillCategory.category}</h4>
            <div className="skill-list">
              {skillCategory.skills.map((skill, index) => (
                <span key={index} className="skill-item">{skill}</span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Skills;