// Import necessary components and functions from react-router-dom.

import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
} from "react-router-dom";

import RootLayout from "./layout/Root.layout";
import PublicLayout from "./layout/Public.layout";
import AdminLayout from "./layout/Admin.layout";
import AuthLayout from "./layout/Auth.layout";

import HomePage from "./pages/public/Home.page";
import LoginPage from "./pages/auth/Login.page";
import SinUpPage from "./pages/auth/SinUp";

export const router = createBrowserRouter(
  createRoutesFromElements(
    <Route element={<RootLayout />}>

      {/*rutas publicas*/}
      <Route element={<PublicLayout />}>
        <Route  index element={<HomePage />}/>
      </Route>

      {/*rutas privadas*/}
      <Route element={<AdminLayout />}>
      </Route>

      {/* rutas de autentificacion */}
      <Route element={<AuthLayout />}>
        <Route path="login" element={<LoginPage/>}/>
        <Route path="sinup" element={<SinUpPage/>}/>
      </Route>



    </Route>
  )
);