import React from 'react';
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';

const GoogleLoginButton = () => {
    const navigate = useNavigate();
    const handleSuccess = (response) => {
        const token = response.credential;
        fetch('http://localhost:3000/api/auth/google', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ token }),
        })
            .then((res) => res.json())
            .then((data) => {
                if (data.user) {
                    localStorage.setItem('user', JSON.stringify(data.user));
                    navigate('/');
                } else {
                    toast.error('Ошибка авторизации через Google');
                }
            })
            .catch((err) => {
                toast.error('Ошибка авторизации через Google');
                console.error('Error during Google login:', err);
            });
    };

    const handleError = () => {
        toast.error('Ошибка авторизации через Google');
    };

    return (
        <GoogleOAuthProvider clientId="361014622495-hvo6p6kt0g531fvl6iv304arnqrl65sv.apps.googleusercontent.com">
            <GoogleLogin
                onSuccess={handleSuccess}
                onError={handleError}
            />
        </GoogleOAuthProvider>
    );
};

export default GoogleLoginButton;