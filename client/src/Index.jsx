import React from 'react'
import ReactDOM from 'react-dom/client'
import {createBrowserRouter, RouterProvider} from "react-router-dom"

import Home from './pages/Home.jsx'
import Profile from './pages/Profile.jsx'
import Games from './pages/Games.jsx'
import Teams from './pages/Teams.jsx'
import Error from './pages/Error.jsx'


import './index.css'




const router = createBrowserRouter([
  {
    path:"/",
    element:<Home/>,
    children: [
      {
        path:"profile",
        element:<Profile/>
      },
      {
        path: "games",
        element: <Games/>
      },
      {
        path:"teams",
        element: <Teams/>
      },
      {
        path:"*",
        element:<Error/>
        
      }
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
)
