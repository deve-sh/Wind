const express = require("express");

const app = express();

app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());

app.get("/", (_, res) =>
	res.status(200).json({
		message: "Health Check.",
	})
);

app.all("*", (_, res) => res.sendStatus(404));

app.listen(process.env.PORT || 8900);
