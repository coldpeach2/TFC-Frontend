import React from "react";
import { useRef, useState, useEffect } from "react"
import { Grid, Paper, Avatar, Typography, TextField, Button } from '@mui/material'
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import Checkbox from '@mui/material/Checkbox';

const EMAIL_REGEX = /^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$/
const PASSWORD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/

const Register = () => {
    const emailRef = useRef()
    const errorRef = useRef()

    const [errorMsg, setErrorMsg] = useState('')
    const [success, setSucess] = useState(false)

    const [email, setEmail] = useState('')
    const [validEmail, setValidEmail] = useState(false)
    const [emailFocus, setEmailFocus] = useState(false)

    const [password, setPassword] = useState('')
    const [validPassword, setValidPasswordl] = useState(false)
    const [passwordFocus, setPasswordFocus] = useState(false)

    const [password2, setPassword2] = useState('')
    const [validPassword2, setValidPassword2] = useState(false)
    const [password2Focus, setPassword2Focus] = useState(false)

    const [firstName, setFirstName] = useState('')
    const [validFirstName, setValidFirstName] = useState(false)
    const [validFirstNameFocus, setValidFirstNameFocus] = useState(false)

    const [lastName, setLastName] = useState('')
    const [validLastName, setValidLastName] = useState(false)
    const [validLastNameFocus, setValidLastNameFocus] = useState(false)

    const [phoneNum, setPhoneNum] = useState('')
    const [validPhoneNum, setValidPhoneNum] = useState(false)
    const [phoneNumFocus, setPhoneNumFocus] = useState(false)

    useEffect(() => {
        emailRef.current ? emailRef.current.focus() : console.log("unfocus")
    }, [])

    useEffect(() => {
        const res = EMAIL_REGEX.test(email)
        console.log(res)
        console.log(email)
        setValidEmail(res)
    }, [email])

    return (
        <section>
            <form>
        <TextField fullWidth 
                   id='firstName'
                   label='first name' 
                   placeholder="Enter your name" />
        <TextField fullWidth 
                   id='lastName'
                   label='last name' 
                   placeholder="Enter your last name" />
        <TextField fullWidth 
                   id='email' 
                   label='email' 
                   placeholder="Enter your email" />
        <TextField fullWidth 
                   id='phoneNum' 
                   label='phone number' 
                   placeholder="Enter your phone number" />
        <TextField fullWidth 
                   id='password' 
                   label='password' 
                   placeholder="Enter your password"/>
        <TextField fullWidth 
                   id='password2' 
                   label='password' 
                   placeholder="Confirm your password"/>
        <FormControlLabel
            control={<Checkbox name="checkedA" />}
            label="I accept the terms and conditions."
        />
        <Button type='submit' variant='contained' color='primary'>Sign up</Button>
        </form>
    </section>
    )


}
export default Register