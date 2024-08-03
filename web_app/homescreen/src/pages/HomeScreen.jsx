import styles from "./HomeScreen.module.css";

const HomeScreen = () => {
  return (
    <div className={styles.homeScreen}>
      <div className={styles.depth0Frame0}>
        <div className={styles.statusBarIphone}>
          <div className={styles.time}>
            <div className={styles.time1}>9:41</div>
          </div>
          <div className={styles.levels}>
            <div className={styles.battery}>
              <div className={styles.border} />
              <img className={styles.capIcon} alt="" src="/cap.svg" />
              <div className={styles.capacity} />
            </div>
            <img className={styles.wifiIcon} alt="" src="/wifi.svg" />
            <img
              className={styles.cellularConnectionIcon}
              alt=""
              src="/cellular-connection.svg"
            />
          </div>
        </div>
        <div className={styles.depth1Frame0}>
          <div className={styles.depth2Frame0}>
            <img
              className={styles.depth3Frame0}
              alt=""
              src="/depth-3-frame-0@2x.png"
            />
          </div>
          <b className={styles.b}>Алексей</b>
        </div>
        <div className={styles.depth1Frame1}>
          <b className={styles.b1}>Объекты рядом</b>
        </div>
        <div className={styles.depth1Frame2}>
          <div className={styles.depth2Frame01}>
            <img
              className={styles.depth3Frame01}
              alt=""
              src="/depth-3-frame-01@2x.png"
            />
            <div className={styles.depth3Frame1}>
              <div className={styles.depth4Frame0}>
                <b className={styles.b2}>Рублевское</b>
              </div>
              <div className={styles.depth4Frame1}>
                <div className={styles.depth5Frame0}>
                  <div className={styles.depth6Frame0}>
                    <div className={styles.div}>
                      Одинцовский г. о.Рублево-Успенское, 21 км
                    </div>
                  </div>
                  <div className={styles.depth6Frame1}>
                    <div className={styles.div}>Застройщик: e.Development</div>
                  </div>
                </div>
              </div>
              <b className={styles.b2}>От 700 ₽ / час</b>
            </div>
          </div>
        </div>
        <div className={styles.depth1Frame3}>
          <div className={styles.depth2Frame02}>
            <div className={styles.depth3Frame02}>
              <div className={styles.depth4Frame01}>
                <b className={styles.b4}>Откликнуться</b>
              </div>
            </div>
            <div className={styles.depth3Frame11}>
              <div className={styles.depth4Frame01}>
                <b className={styles.b4}>Подробнее</b>
              </div>
            </div>
          </div>
        </div>
        <div className={styles.depth1Frame4}>
          <div className={styles.depth2Frame01}>
            <img
              className={styles.depth3Frame01}
              alt=""
              src="/depth-3-frame-02@2x.png"
            />
            <div className={styles.depth3Frame12}>
              <div className={styles.depth4Frame0}>
                <b className={styles.b2}>КП “Раздоры 2”</b>
              </div>
              <div className={styles.depth4Frame1}>
                <div className={styles.depth5Frame0}>
                  <div className={styles.depth6Frame0}>
                    <div className={styles.div}>
                      Красногорск г. о.Новорижское, 9 км
                    </div>
                  </div>
                  <div className={styles.depth6Frame11}>
                    <div className={styles.div}>Застройщик: e.Development</div>
                  </div>
                </div>
              </div>
            </div>
            <b className={styles.b7}>От 900 ₽ / час</b>
          </div>
        </div>
        <div className={styles.depth1Frame3}>
          <div className={styles.depth2Frame02}>
            <div className={styles.depth3Frame02}>
              <div className={styles.depth4Frame01}>
                <b className={styles.b4}>Откликнуться</b>
              </div>
            </div>
            <div className={styles.depth3Frame11}>
              <div className={styles.depth4Frame01}>
                <b className={styles.b4}>Подробнее</b>
              </div>
            </div>
          </div>
        </div>
        <div className={styles.depth1Frame6} />
      </div>
    </div>
  );
};

export default HomeScreen;
