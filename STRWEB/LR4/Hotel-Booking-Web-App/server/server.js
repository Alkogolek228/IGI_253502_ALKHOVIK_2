const express = require('express');
const cors = require('cors');
const { graphqlHTTP } = require('express-graphql');
const mongoose = require('mongoose');
const schema = require("./schemas/Schema.js");
const isAuth = require('./middlewares/isAuth.js');
const dotenv = require('dotenv');
const { OAuth2Client } = require('google-auth-library');
const User = require('./models/User');

const app = express();
app.use(cors());
app.use(express.json());
app.use(isAuth);
dotenv.config();

const mongoURL = process.env.MONGO_URL;
mongoose.connect(mongoURL, {
    useNewUrlParser: true,
    useUnifiedTopology: true
});
mongoose.connection.once('open', () => console.log("DB Connected..."));

const client = new OAuth2Client(process.env.GOOGLE_CLIENT_ID);

app.post('/api/auth/google', async (req, res) => {
    const { token } = req.body;
    try {
        const ticket = await client.verifyIdToken({
            idToken: token,
            audience: process.env.GOOGLE_CLIENT_ID,
        });
        const payload = ticket.getPayload();
        const { sub, email, name } = payload;

        let user = await User.findOne({ email });
        if (!user) {
            user = new User({
                googleId: sub,
                email,
                name,
                accessToken: '',
                refreshToken: '',
                accessTokenExp: '',
                refreshTokenExp: '',
                isAdmin: false,
                isManager: false,
                isBlocked: false,
                joined: new Date(),
            });
            await user.save();
        }

        res.status(200).json({ user });
    } catch (error) {
        console.error('Error verifying Google token:', error);
        res.status(400).json({ error: 'Invalid token' });
    }
});

app.use("/graphql", graphqlHTTP({
    schema,
    graphiql: true,
    customFormatErrorFn: (err) => {
        console.error('GraphQL Error:', err);
        return { message: err.message, locations: err.locations, path: err.path };
    }
}));

const port = process.env.PORT || 3000;
app.listen(port, () => console.log("Server is running..."));
app.get('/', (req, res) => res.send("Auth system..."));