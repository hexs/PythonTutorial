## Tutorial

1. `windows + r` > `powershell` > Enter

   `output >` PS C:\Users\<user>

2. change dir

   ``` shell
   cd c:\
   ```

   `output >` PS C:\

3. create folder

    ```shell
    mkdir PythonProjects
    ```

4. create venv

   ```shell
   python -m venv .venv
   ```

5. activate venv

   ```shell
   .venv\Scripts\activate
   ```

6. install packages
    - pip install --proxy scheme://proxy_server_ip:port packages_name
        ``` shell
        pip install numpy
        ```

    - if using a Proxy Server
        - pip install --proxy scheme://proxy_server_ip:port packages_name
        - or
        - pip install --proxy scheme://user:pass@proxy_server_ip:port packages_name

    - example : install numpy
        ``` shell
        pip install --proxy http://150.61.8.70:10086 numpy
        ```

        ``` shell
        pip install --proxy http://<user>:<pass>@150.61.8.70:10086 numpy
        ```

7. install `opencv-python` and `hexss`