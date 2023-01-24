import React from "react";
import { Button, Form } from "semantic-ui-react";
import { useFormik } from "formik";
import * as Yup from "yup"
import { toast } from "react-toastify";
import "./LoginForm.scss";


export function LoginForm() {
    const formik= useFormik({
        initialValues: initialValues(),
        validationSchema: Yup.object(validationSchema()),
        onSubmit: async(formValue) => {
            try{
                console.log("salida")
            }catch (error) {
                toast.error(error.message);
            }
        },
    });
  return (
    <Form ClassName="login-form-admin" onSubmit={formik.handleSubmit}>
        <Form.Input name ="email" placeholder="correo electronico" value={formik.values.email}
        onChange= {formik.handleChange}
        error={formik.email}
        />
        <Form.Input name="password" type = "password" placeholder="contraseña"
        value={formik.values.password}
        onChange= {formik.handleChange}
        error={formik.errors.password}
        />
        <Button type="submit" content="Iniciar Sesion" primary fluid />

        
    </Form>
        
    
  );
}

function initialValues(){
    return{
        email:"",
        password:"",
    };
}
function validationSchema(){
    return{
        email:Yup.string().email(true).required(true),
        password:Yup.string().required(true)
    };
}

