import Navbar from '../components/Navbar'
import { Outlet } from 'react-router-dom'


function Home() {

  return (
    <>
      <Navbar/>
      <Outlet/>
      <div style={{backgroundColor:"black", border:"1px"} }></div>
    </>
  )
}

export default Home
