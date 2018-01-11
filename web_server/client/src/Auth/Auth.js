class Auth {
    static authenticateUser(token, email){
        localStorage.setItem('token', token);
        // use email as the user name
        localStorage.setItem('email', email);
    }

    static isUserAuthenticated(){
        // tell whether token exists in the server
        return localStorage.getItem('token') != null;
    }
    // log out
    static deauthenticateUser(){
        localStorage.removeItem('token');
        localStorage.removeItem('email');
    }

    static getToken() {
        return localStorage.getItem('token');
    }

    static getEmail() {
        return localStorage.getItem('email');
    }
}

export default Auth;