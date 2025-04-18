mkdir -p ~/.streamlit/

echo "\
[general]
email = \"travelvector121@gmail.com\"

[server]
headless = true
enableCORS = false
port = \$PORT
" > ~/.streamlit/config.toml
