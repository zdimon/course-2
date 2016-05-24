##Gitignore

    find . -name "*.pyc" -exec rm -rf {} \;
    echo '*.pyc' >> .gitignore
    git add --all
    git commit -m 'delete .pyc'
    git push
    


    
