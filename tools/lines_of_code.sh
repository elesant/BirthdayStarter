BASE_PATH=..

find $BASE_PATH -name "*.py" -o -name "*.html" | grep -v "/venv/" | grep -v "/migrations/" | xargs wc -l | sort -n

echo -n "Lines of Python:"
find $BASE_PATH -name "*.py" | grep -v "/venv/" | grep -v "/migrations/" | xargs wc -l | tail -1

echo -n "Lines of HTML:"
find $BASE_PATH -name "*.html" | grep -v "/venv/" | grep -v "/migrations/" | xargs wc -l | tail -1
