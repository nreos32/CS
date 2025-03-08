const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 8000;

app.use(cors({
  origin: 'http://localhost:5173'
}));

const educationData = [
  {
    id: 1,
    institution: "Humber College (North Campus)",
    degree: "Computer Programming Program",
    year: "2023-present",
    description: "Studying front end and back end development in order to be a fullstack specialist"
  },
  {
    id: 2,
    institution: "trytohackme.com",
    degree: "Cyber Security",
    year: "2024-2024",
    description: "Learning offensive and defensive cyber security"
  }
];

const experienceData = [
  {
    id: 1,
    company: "Blender Work",
    position: "3D Modeling with Blender",
    year: "2024-present",
    description: "Sculping and modeling 3D objects for commisions and personal projects"
  },
  {
    id: 2,
    company: "Unity",
    position: "Game Design",
    year: "2023-present",
    description: "Basic game design making top down games"
  },
  {
  id: 3,
    company: "Blender Work",
    position: "3D Modeling with Blender",
    year: "2024-present",
    description: "Sculping and modeling 3D objects for commisions and personal projects"
  }
];

const overviewData = {
  name: "Nicholas Maroudas (n01417500)",
  title: "Full Stack Developer"
};

const skillsData = [
  {
    id: 1,
    category: "Frontend",
    skills: ["HTML", "CSS", "JavaScript", "React"]
  },
  {
    id: 2,
    category: "Backend",
    skills: ["Node.js", "Express", "MongoDB", "MySQL"]
  },
  {
    id: 3,
    category: "Tools",
    skills: ["GitHub", "VS Code", "npm", "Unity", "Blender", "Aseprite" ,"IDA Pro", "JEB Decompiler"]
  },
  {
    id: 4,
    category: "Other Languages",
    skills: ["C++", "C#", "Python", "Java"]
  }
];

app.get('/getEdu', (req, res) => {
  res.json(educationData);
});

app.get('/getExp', (req, res) => {
  res.json(experienceData);
});

app.get('/getOverview', (req, res) => {
  res.json(overviewData);
});

app.get('/getSkills', (req, res) => {
  res.json(skillsData);
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});