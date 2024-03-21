import numpy as np
import pandas as pd


def haversine_distance(lon: float, lat: float, df_lon: pd.Series, df_lat: pd.Series) -> pd.Series:
    """
    使用Haversine公式计算两个地点之间的距离。

    参数：
    df_lon : pd.Series
        包含经度数据的Series。
    df_lat : pd.Series
        包含纬度数据的Series。
    lon : float
        参考点的经度。
    lat : float
        参考点的纬度。

    返回：
    pd.Series
        包含距离数据的Series。距离单位为千米。
    """
    if len(df_lon) != len(df_lat):
        raise ValueError("Lengths of df_lon and df_lat must be the same")

    if not (-180 <= lon <= 180):
        raise ValueError("Longitude must be in the range [-180, 180]")
    if not (-90 <= lat <= 90):
        raise ValueError("Latitude must be in the range [-90, 90]")

    # 将经度和纬度转换为弧度
    lon_rad = np.radians(df_lon)
    lat_rad = np.radians(df_lat)
    d_lon = lon_rad - np.radians(lon)
    d_lat = lat_rad - np.radians(lat)

    distance = 2 * 6371 * np.arcsin(
        np.sqrt(
            np.sin(d_lat / 2) ** 2 +
            np.cos(lat_rad) * np.cos(np.radians(lat)) * np.sin(d_lon / 2) ** 2
        )
    )

    return distance
