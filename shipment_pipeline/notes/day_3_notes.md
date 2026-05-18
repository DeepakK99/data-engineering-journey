# day 3 notes (basic pipeline)

## project structure
- /data
- /logs (important)
- /src (core components)
- requirements.txt
- readme.md


## Pipeline stucture
- reader
- cleaner (stream)
- validator
- transformer 
- writer (stream)

## flow
- create a entry point (main.py)
- orchestrate the components of the pipeline
- example: read -> clean -> validate -> transform -> write
