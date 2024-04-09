import React from 'react'
import ReactDOM from 'react-dom/client'
import {createBrowserRouter, RouterProvider} from "react-router-dom"

import App from './pages/App.jsx'
import Games from './pages/Games.jsx'
import Error from './pages/Error.jsx'


import './index.css'




const router = createBrowserRouter([
  {
    path:"/",
    element:<App/>,
    children: [
      {
        path: "games",
        element: <Games/>
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
