for file in ./*
do
    flask --app $file run
done