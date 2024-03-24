# GIT & GITHUB
## Sample of Git Push and .gitignore

```txt
$ git clone https://github.com/FariusGitHub/temp.git
	Cloning into 'temp'...
	remote: Enumerating objects: 20, done.
	remote: Counting objects: 100% (20/20), done.
	remote: Compressing objects: 100% (15/15), done.
	remote: Total 20 (delta 3), reused 9 (delta 0), pack-reused 0
	Unpacking objects: 100% (20/20), 119.56 KiB | 979.00 KiB/s, done.

$ cd temp
$ ls
	image1.png  image2.png  image3.png

$ nano .gitignore
$ nano to_add.txt

$ git reset .gitignore
	ft@ft:~/devops/temp$ git status
	On branch main
	Your branch is up to date with 'origin/main'.

	Changes to be committed:
	  (use "git restore --staged <file>..." to unstage)
		new file:   to_add.txt

	Untracked files:
	  (use "git add <file>..." to include in what will be committed)
		.gitignore

ft@ft:~/devops/temp$ git commit -m 'push'
	[main f6938de] push
	 1 file changed, 1 insertion(+)
	 create mode 100644 to_add.txt


$ git remote set-url origin https://ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX@github.com/FariusGitHub/temp
$ git push origin main
	Enumerating objects: 4, done.
	Counting objects: 100% (4/4), done.
	Delta compression using up to 8 threads
	Compressing objects: 100% (2/2), done.
	Writing objects: 100% (3/3), 274 bytes | 274.00 KiB/s, done.
	Total 3 (delta 1), reused 0 (delta 0)
	remote: Resolving deltas: 100% (1/1), completed with 1 local object.
	To https://github.com/FariusGitHub/temp
	   fa88f70..f6938de  main -> main

$ git push origin main
	Everything up-to-date

$ git tag
	v1.0

```

