from prefect.deployments import run_deployment


def main():
    response = run_deployment(name="main-flow/taxi-hw", parameters={"train_path" : "Homeworks/Homework3/data/green_tripdata_2023-01.parquet", "val_path" : "Homeworks/Homework3/data/green_tripdata_2023-02.parquet"})
    print(response)


if __name__ == "__main__":
   main()
