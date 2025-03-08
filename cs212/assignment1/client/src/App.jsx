import { useState, useEffect } from 'react'
import { Container } from 'react-bootstrap'
import Header from './components/Header'
import Education from './components/Education'
import Experience from './components/Experience'
import Skills from './components/Skills'
import Footer from './components/Footer'
import axios from 'axios'

function App() {
  const [overview, setOverview] = useState(null)
  const [education, setEducation] = useState([])
  const [experience, setExperience] = useState([])
  const [skills, setSkills] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const overviewRes = await axios.get('http://localhost:8000/getOverview')
        const educationRes = await axios.get('http://localhost:8000/getEdu')
        const experienceRes = await axios.get('http://localhost:8000/getExp')
        const skillsRes = await axios.get('http://localhost:8000/getSkills')

        setOverview(overviewRes.data)
        setEducation(educationRes.data)
        setExperience(experienceRes.data)
        setSkills(skillsRes.data)
        setLoading(false)
      } catch (error) {
        console.error('Error fetching data:', error)
        setError('Failed to fetch resume data. Please try again later.')
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  if (loading) {
    return (
      <Container className="text-center py-5">
        <h2>Loading resume data...</h2>
      </Container>
    )
  }

  if (error) {
    return (
      <Container className="text-center py-5">
        <h2>Error</h2>
        <p>{error}</p>
      </Container>
    )
  }

  return (
    <div className="App">
      {overview && <Header overview={overview} />}
      
      <Container>
        <Experience experience={experience} />
        <Education education={education} />
        <Skills skills={skills} />
      </Container>
      
      <Footer />
    </div>
  )
}

export default App